import { Component } from '@angular/core';
import {SlimLoadingBarService} from 'ng2-slim-loading-bar';
import {
  NavigationCancel,
  Event,
  NavigationEnd,
  NavigationError,
  NavigationStart,
  Router, ActivatedRoute
} from '@angular/router';
import {BlogService} from "./blog.service";
import Article from "./article";
        
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Blog';
  sort: string;
  keyword: string;
  search_by: string;
  articles: Article[];

  constructor(private loadingBar: SlimLoadingBarService,
              private router: Router,
              private bs: BlogService,) {
    this.router.events.subscribe((event: Event) => {
      this.navigationInterceptor(event);
    });
  }
  private navigationInterceptor(event: Event): void {
    if (event instanceof NavigationStart) {
      this.loadingBar.start();
    }
    if (event instanceof NavigationEnd) {
      this.loadingBar.complete();
    }
    if (event instanceof NavigationCancel) {
      this.loadingBar.stop();
    }
    if (event instanceof NavigationError) {
      this.loadingBar.stop();
    }
  }

  testSearch() {
    this.router.navigate(['search'], {
      queryParams: {
        keyword: '123',
      }
    })
  }
}
