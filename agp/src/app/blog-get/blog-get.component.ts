import { Component, OnInit } from '@angular/core';
import Article from '../article';
import { BlogService } from '../blog.service';

@Component({
  selector: 'app-blog-get',
  templateUrl: './blog-get.component.html',
  styleUrls: ['./blog-get.component.css']
})
export class BlogGetComponent implements OnInit {

  articles: Article[];
  constructor(private bs: BlogService) { }

  ngOnInit() {
    this.bs
      .getArticles()
      .subscribe((data: Article[]) => {
        this.articles = data;
      });
  }

  deleteArticle(id) {
    this.bs.deleteArticle(id).subscribe(res => {
      this.articles.splice(id, 1);
    });
  }
}
