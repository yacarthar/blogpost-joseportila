import {Injectable} from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {map} from 'rxjs/operators';
import {Observable} from 'rxjs';

export class ArticleItem {
	constructor(
		public title: string,
        public url: string,
        public path: string,
        public pid: string,
        public time: string,
        public content: string
	){}
}

@Injectable()
export class BlogService {
	apiRoot: string = "http://127.0.0.1:5000/post";
	constructor(private http: HttpClient){}

	showAll(): Observable<ArticleItem[]> {
		let apiURL = this.apiRoot;
		return this.http.get(apiURL).pipe(
			map((res: any) => {
				return res.result.map(item => {
					return new ArticleItem(
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
}