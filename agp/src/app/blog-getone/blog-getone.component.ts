import { Component, OnInit } from '@angular/core';
import Article from '../article';
import { BlogService } from '../blog.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-blog-getone',
  templateUrl: './blog-getone.component.html',
  styleUrls: ['./blog-getone.component.css']
})
export class BlogGetoneComponent implements OnInit {
  article: Article;
  constructor(private bs: BlogService,
               private route: ActivatedRoute) { }
  url = this.route['_routerState'].snapshot.url;
  id = this.url.slice(this.url.lastIndexOf('/')+1);

  ngOnInit() {
    this.bs
      .getOneArticle(this.id)
      .subscribe((item: any) => {
        this.article = new Article(
          item.title,
          item.url,
          item.path,
          item.pid,
          item.time,
          item.content
        )
      });
  }

}

