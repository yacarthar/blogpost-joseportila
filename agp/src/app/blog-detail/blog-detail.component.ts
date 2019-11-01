import { Component, OnInit, NgModule, Inject } from '@angular/core';
import { HttpService } from  '../shared/service';
import { ActivatedRoute } from '@angular/router';
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
  selector: 'app-blog-detail',
  templateUrl: './blog-detail.component.html',
  styleUrls: ['./blog-detail.component.css']
})
export class BlogDetailComponent implements OnInit {
	content: string;
	path: string;
	pid: string;
	time: string;
	title: string;
	url: string;
  current_url = this.route['_routerState'].snapshot.url;
  id = this.current_url.slice(this.current_url.lastIndexOf('/')+1);

  constructor (
	  private hs: HttpService,
	  private route: ActivatedRoute
  ) {}

  ngOnInit() {
  	this.hs.getOneArticle(this.id)
  	.subscribe((res: article) => {
  		this.content = res['content'];
  		this.path = res['path'];
  		this.pid = res['pid'];
  		this.time = res['time'];
  		this.title = res['title'];
  		this.url = res['url'];
  	});
  }

}
