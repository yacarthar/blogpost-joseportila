import { Component, OnInit } from '@angular/core';
import { BlogService, ArticleItem } from './blog.service';
import {Observable} from 'rxjs';

@Component({
  selector: 'app-blog',
  templateUrl: './blog.component.html',
  styleUrls: ['./blog.component.css'],
  providers: [BlogService]
})
export class BlogComponent implements OnInit {
  private blogs: Observable<ArticleItem[]>;
  private loading: boolean = false;

  constructor(private blogService: BlogService) {}

  ngOnInit() {
    this.loading = true;
    this.blogs = this.blogService.showAll();
  }
  onSearch() {
    this.blogs = this.blogService.showAll('xxx');
  }

}
