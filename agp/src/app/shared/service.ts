import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";

// import {HttpParams} from "@angular/common/http";



@Injectable({
  providedIn: 'root'
})


export class HttpService {
  mes: string;
  uri: string = `http://127.0.0.1:5000/post`;
  constructor(private http: HttpClient) { }

  getArticles(url) {
    return this.http.get(url)
  }

  getOneArticle(id) {
    return this.http.get(this.uri + '/' + id)
  }

  addArticle(title, content, callback) {
    const obj = {
      'title': title,
      'content': content
    };
    this.http.post(this.uri, obj).subscribe(
      res => {
        this.mes = res['message']
        callback(this.mes);
      });
  }

  updateArticle(title, content, id, callback) {
    const obj = {
      'title': title,
      'content': content
    };
    return this.http.put(this.uri + '/' + id, obj)
        .subscribe(res => {
        this.mes = res['message']
        console.log(`Update: ` + this.mes);
        // callback.bind(this)(arg);
        callback(this.mes);
      });
  }

  deleteArticle(id, callback) {
    return this.http.delete(this.uri + '/' + id)
        .subscribe(res => {
        this.mes = res['message']
        console.log(`Delete: ` + this.mes);
        callback(this.mes);
      });
  }

}