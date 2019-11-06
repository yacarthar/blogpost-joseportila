import { Component, OnInit, NgModule, Inject } from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material';
import { ActivatedRoute, Router } from '@angular/router';

import { ModalComponent } from '../modal/modal.component';
import { ModalEditComponent } from '../modal-edit/modal-edit.component';
import { ModalDeleteComponent } from '../modal-delete/modal-delete.component';
import { HttpService } from  '../shared/service';
import { NotifierService } from 'angular-notifier';

class article {
    constructor(
        public content: string,
        public path: string,
        public pid: string,
        public time: string,
        public title: string,
        public url: string
    ) {}
}

@Component({
    selector: 'app-blog-list',
    templateUrl: './blog-list.component.html',
    styleUrls: ['./blog-list.component.css']
})
export class BlogListComponent implements OnInit {
    titleCreateModal: string;
    contentCreateModal: string;
    titleEditModal: string;
    contentEditModal: string;
    deleteModal: boolean;

    page_num: string;
    page_size: string;

    result_total: number;
    page_total: number;
    current_page: string;
    first_page: string;
    last_page: string;
    next_page: string;
    previous_page: string;
    results: Array<article>;

    display: boolean;

    search_by: string;
    keyword: string;
    sort: string;



    constructor(
        public dialog: MatDialog,
        private hs: HttpService,
        private route: ActivatedRoute,
        private router: Router,
        private notifier: NotifierService,
    ) {}

    parseData(path) {
        // this.display = false;
        var url = 'http://127.0.0.1:5000';
        this.hs.getArticles(url + path)
            .subscribe(data => {
                this.result_total = data['result_total'];
                this.current_page = data['current_page'];
                this.first_page = data['pagination']['first_page'];
                this.last_page = data['pagination']['last_page'];
                this.next_page = data['pagination']['next_page'];
                this.previous_page = data['pagination']['previous_page'];
                this.page_total = ((this.result_total % parseInt(this.page_size, 10) == 0)?
                        Math.floor(this.result_total/parseInt(this.page_size, 10))
                        : Math.floor(this.result_total/parseInt(this.page_size, 10)) + 1
                );
                this.page_num = this.current_page.slice(
                    this.current_page.indexOf('page=') + 5, this.current_page.indexOf('&')
                )
                this.results = data['result'].map(
                    item => {return new article(
                        item['content'],
                        item['path'],
                        item['pid'],
                        item['time'],
                        item['title'],
                        item['url']
                    );
                    }
                );
                console.log(this.results);
                console.log(url+path);
                this.display = true;
            });
    }

    ngOnInit(): void {
        this.route.queryParamMap.subscribe(queryParams => {
            this.page_num = queryParams.get("page");
            if (!this.page_num ) {this.page_num='1'}
            this.page_size = queryParams.get("size");
            if (!this.page_size) {this.page_size='5'}
            console.log(this.page_num);
            this.keyword = queryParams.get("keyword");
            console.log(this.keyword);
            this.search_by = queryParams.get("search_by");
            console.log(this.search_by);
            this.sort = queryParams.get("sort");
            console.log(this.sort);
        })
        if (!(!this.keyword || this.keyword.length === 0 || !this.keyword.trim() )) {
            this.parseData(`/post/search`
                +`?page=${this.page_num}`
                +`&size=${this.page_size}`
                +`&keyword=${this.keyword}`
                +`&search_by=${this.search_by}`
                +`&sort=${this.sort}`
            )
        } else {
                this.parseData(`/post?page=${this.page_num}&size=${this.page_size}`);
            }
    }

    nextClick() {
        this.parseData(this.next_page);
        this.router.navigateByUrl(this.next_page); 
    }

    prevClick() {
        this.parseData(this.previous_page);
        this.router.navigateByUrl(this.previous_page);
    }

    firstPageClick() {
        this.parseData(this.first_page);
        this.router.navigateByUrl(this.first_page);
    }

    lastPageClick() {
        this.parseData(this.last_page);
        this.router.navigateByUrl(this.last_page);
    }

    searchClick() {
        var url = `/post/search`;
        var param: any = {};

        if (!(!this.keyword || this.keyword.length === 0 || !this.keyword.trim() )) {
            url += `?keyword=${this.keyword}`;
            param['keyword'] = this.keyword;
            if (this.search_by && this.search_by != "") {
                url += `&search_by=${this.search_by}`;
                param['search_by'] = this.search_by;
            };
            if (this.sort && this.sort != "") {
                url += `&sort=${this.sort}`;
                param['sort'] = this.sort;
            };
            this.router.navigate([`/post`], {queryParams:param});
            this.parseData(url);
        }
    }

    homeClick() {
        this.parseData('/post');
        this.router.navigateByUrl('/post');
    }
    
    openCreateDialog(): void {
        const dialogRef = this.dialog.open(ModalComponent, {
            width: '960px',
            height: '400px',
            disableClose: true,
            data: {title: this.titleCreateModal = '', content: this.contentCreateModal=''}
        });

        dialogRef.afterClosed().subscribe(result => {
            if (result) {
                this.titleCreateModal = result.title;
                console.log(this.titleCreateModal);
                this.contentCreateModal = result.content
                console.log(this.contentCreateModal);
                this.hs.addArticle(this.titleCreateModal, this.contentCreateModal,(mes) => {
                        this.notifier.notify('info', mes);
                        this.parseData('/post');
                        this.router.navigateByUrl('/post');
                    }
                )

            }
        });
    }



    openEditDialog(pid, title, content): void {
        const dialogRef = this.dialog.open(ModalEditComponent, {
            width: '960px',
            height: '400px',
            disableClose: true,
            data: {
                title: this.titleEditModal = title,
                content: this.contentEditModal = content
            }
        });

        dialogRef.afterClosed().subscribe(result => {
            if (result) {
                this.titleEditModal = result.title;
                console.log(`imput title:: ` + this.titleEditModal);
                this.contentEditModal = result.content
                console.log(`imput content: ` + this.contentEditModal);
                this.hs.updateArticle(this.titleEditModal,this.contentEditModal,pid,
                    (mes) => {
                        this.notifier.notify('info', mes);
                        this.parseData(this.current_page);
                    });
            }
        });
    }

    openDeleteDialog(pid): void {
        const dialogRef = this.dialog.open(ModalDeleteComponent, {
            disableClose: true,
            width: '250px',
            height: '150px',
            data: Boolean
        });

        dialogRef.afterClosed().subscribe((result: any) => {
            // console.log(result)})
            if (result) {
                console.log(result)
                this.hs.deleteArticle(pid, (mes) => {
                    this.notifier.notify('info', mes);
                    this.parseData(this.current_page);
                });
            };
        });
    }

    goDetail(id) {
        this.router.navigate([`/detail/${id}`], {
            queryParams:{'from': `${this.current_page}`}
        });
    }
}
