import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {map} from 'rxjs/operators';
// import {HttpParams} from "@angular/common/http";

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

  searchArticles(keyword, search_by, sort) {
    let params: any = {};
    if (keyword != undefined) {
      params['keyword'] = keyword;
    }
    if (sort != undefined) {
      params['sort'] = sort;
    }
    if (search_by != undefined) {
      params['search_by'] = search_by;
    }

    return this.http.get(`${this.uri}/search`, {params: params}).pipe(
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

  addArticle(ArticleTitle, ArticlePath, ArticlePid) {
    console.log(ArticleTitle, ArticlePath, ArticlePid);
    const obj = {
      'title': ArticleTitle,
      'path': ArticlePath,
      'pid':ArticlePid
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