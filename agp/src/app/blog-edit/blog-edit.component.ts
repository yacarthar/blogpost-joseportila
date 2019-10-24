import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { BlogService } from '../blog.service';

@Component({
  selector: 'app-blog-edit',
  templateUrl: './blog-edit.component.html',
  styleUrls: ['./blog-edit.component.css']
})
export class BlogEditComponent implements OnInit {

  angForm: FormGroup;
  article: any = {};

  constructor(private route: ActivatedRoute,
    private router: Router,
    private bs: BlogService,
    private fb: FormBuilder
    ){
      this.createForm();
    }

  createForm() {
    this.angForm = this.fb.group({
      articleTitle: ['', Validators.required ],
      articlePath: ['', Validators.required ],
      articlePid: ['', Validators.required ]
    });
  }

  ngOnInit() {
    // this.route.params.subscribe(params => {
    //     this.bs.updateArticle(params.id).subscribe(res => {
    //       this.article = res;
    //   });
    // });
  }

  updateArticle(ArticleTitle, ArticlePath, ArticlePid, id) {
    this.route.params.subscribe(params => {
      this.bs.updateArticle(ArticleTitle, ArticlePath, ArticlePid, params.id);
      this.router.navigate(['Articles']);
    });
  }
}