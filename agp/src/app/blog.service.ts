import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {map} from 'rxjs/operators';

import Article from './article';

@Injectable({
  providedIn: 'root'
})


export class BlogService {
  uri = 'http://127.0.0.1:5000/post';
  constructor(private http: HttpClient) { }

  getArticles() {
    return this.http.get(`${this.uri}`).pipe(
      map((res: any) => {
        return res.result.map(item => {
          return new Article(
            item.title,
            item.url,
            item.path,
            item.pid,
            item.time,
            item.content
          )
        })
      })
    )
  }

  getOneArticle(id) {
    return this.http.get(`${this.uri}/${id}`)
  }

  addArticle(ArticleTitle, ArticlePath, ArticlePid) {
    console.log(ArticleTitle, ArticlePath, ArticlePid);
    const obj = {
      ArticleTitle,
      ArticlePath,
      ArticlePid
    };
    this.http.post(`${this.uri}`, obj)
        .subscribe(res => console.log('Done'));
  }

  updateArticle(ArticleTitle, ArticlePath, ArticlePid, id) {
    const obj = {
      ArticleTitle,
      ArticlePath,
      ArticlePid
    };
    this.http.put(`${this.uri}/${id}`, obj)
        .subscribe(res => console.log('Update Complete'));
  }

  deleteArticle(id) {
    return this.http.delete(`${this.uri}/${id}`);
  }

}