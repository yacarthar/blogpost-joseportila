import { Component, OnInit, NgModule, Inject, ChangeDetectorRef } from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material';

import { ModalComponent } from '../modal/modal.component';
import { ModalEditComponent } from '../modal-edit/modal-edit.component';
import { ModalDeleteComponent } from '../modal-delete/modal-delete.component';
import { HttpService } from  '../shared/service';


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

	result_total: number;
  page_total: number;
	current_page: number;
	first_page: string;
	last_page: string;
	next_page: string;
	previous_page: string;
  results: Array<article>;

  display: boolean;

  search_by: string = 'title';
  keyword: string;
  sort: string = 'date';

  x: boolean;

  constructor(
  	public dialog: MatDialog,
    private hs: HttpService,
    public cd: ChangeDetectorRef,
  ) {}

  parseData(path) {
    this.display = false;
    var url = 'http://127.0.0.1:5000';
    this.hs.getArticles(url + path)
    .subscribe(data => {
      this.result_total = data['result_total'];
      this.current_page = data['current_page'];
      this.first_page = data['pagination']['first_page'];
      this.last_page = data['pagination']['last_page'];
      this.next_page = data['pagination']['next_page'];
      this.previous_page = data['pagination']['previous_page'];
      this.x = false;
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
      this.page_total = Math.floor(this.result_total/5) + 1;
      console.log(this.results);
      console.log(url+path);
    this.display = true;
    });
  }

  ngOnInit(): void {
    this.parseData('/post');
  }

  nextClick() {
		this.parseData(this.next_page);
	}

  prevClick() {
    this.parseData(this.previous_page);
  }

  firstPageClick() {
    this.parseData(this.first_page);
  }

  lastPageClick() {
    this.parseData(this.last_page);
  }

  searchClick() {
    console.log(this.sort);
    console.log(this.search_by);
    console.log(this.keyword);
    this.parseData(`/post/search` +
      `?keyword=${this.keyword}` +
      `&search_by=${this.search_by}` +
      `&sort=${this.sort}`);
  }

  openCreateDialog(): void {
    const dialogRef = this.dialog.open(ModalComponent, {
      width: '720px',
      height: '480px',
      data: {title: this.titleCreateModal, content: this.contentCreateModal}
    });

    dialogRef.afterClosed().subscribe(result => {
      if (result) {
        this.titleCreateModal = result.title;
        console.log(this.titleCreateModal);
        this.contentCreateModal = result.content
        console.log(this.contentCreateModal);
        this.hs.addArticle(this.titleCreateModal, this.contentCreateModal);

      }
    });
  }

  openEditDialog(pid, title, content): void {
    const dialogRef = this.dialog.open(ModalEditComponent, {
      width: '960px',
      height: '400px',
      data: {
        title: this.titleEditModal = title,
        content: this.contentEditModal = content
      }
    });

    dialogRef.afterClosed().subscribe(result => {
      if (result) {
          this.titleEditModal = result.title;
          console.log(this.titleEditModal);
          this.contentEditModal = result.content
          console.log(this.contentEditModal);
          this.hs.updateArticle(this.titleEditModal, this.contentEditModal, pid);
          this.parseData(`/post?page=` + this.current_page);
        }
    });
  }

  openDeleteDialog(pid): void {
    const dialogRef = this.dialog.open(ModalDeleteComponent, {
      width: '200px',
      height: '150px',
    });
    // console.log(pid);
    // console.log(dialogRef);

    dialogRef.afterClosed().subscribe(result => {
      this.hs.deleteArticle(pid);
      // console.log(result);
        
    });
  }
}
