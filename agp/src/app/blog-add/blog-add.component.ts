import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { BlogService } from '../blog.service';

@Component({
  selector: 'app-blog-add',
  templateUrl: './blog-add.component.html',
  styleUrls: ['./blog-add.component.css']
})

export class BlogAddComponent implements OnInit {

  angForm: FormGroup;
  constructor(private fb: FormBuilder, private bs: BlogService) {
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
    this.bs.addArticle(ArticleTitle, ArticlePath, ArticlePid);
  }

  ngOnInit() {
  }

}
