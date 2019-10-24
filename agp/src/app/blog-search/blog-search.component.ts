import { Component, OnInit } from '@angular/core';
import { BlogService } from '../blog.service';
import { ActivatedRoute } from '@angular/router';
import Article from "../article";

@Component({
  selector: 'app-blog-search',
  templateUrl: './blog-search.component.html',
  styleUrls: ['./blog-search.component.css']
})
export class BlogSearchComponent implements OnInit {
  keyword: string;
  search_by: string;
  sort: string;
  articles: Article[] = [];
  displaySearch: boolean;
  constructor(private bs: BlogService,
              private route: ActivatedRoute) {
    this.route.params.subscribe(params=>
       {
         this.sort=params["sort"];
         this.keyword=params["keyword"];
         this.search_by=params["search_by"];
       });
  }
  sub1;
  searchPage() {
    this.sub1 = this.bs
      .searchArticles(this.keyword, this.search_by, this.sort)
      .subscribe((data: Article[]) => {
        this.articles = data;
        console.log(data);
      });
    this.displaySearch=true;
  }

  ngOnInit() {
    this.displaySearch=false;

    this.sub2 = this.route.queryParams.subscribe((params) => {
      console.log('params', params);
    });

    let kw = this.route.snapshot.queryParamMap.get('keyword');
    console.log('keyword', kw);
  }

  ngOnDestroy() {
      this.sub1.unsubscribe();
  }
}
