import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { BlogService } from '../blog.service';

@Component({
  selector: 'app-blog-add',
  templateUrl: './blog-add.component.html',
  styleUrls: ['./blog-add.component.css']
})

export class BlogAddComponent implements OnInit {

  angForm: FormGroup;
  constructor(private fb: FormBuilder,
              private bs: BlogService,
              private router: Router) {
    this.createForm();
  }

  createForm() {
    this.angForm = this.fb.group({
      ArticleTitle: ['', Validators.required ],
      ArticlePath: ['', Validators.required ],
      ArticlePid: ['', Validators.required ]
    });
  }

  addArticle(ArticleTitle, ArticlePath, ArticlePid) {
    this.angForm.controls.ArticleTitle.value;
    this.bs.addArticle(ArticleTitle, ArticlePath, ArticlePid);
    this.router.navigate(['post/', ArticlePid]);
  }

  ngOnInit() {
  }

}
