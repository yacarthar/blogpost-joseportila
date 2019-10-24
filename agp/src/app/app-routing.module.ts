import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { BlogAddComponent } from './blog-add/blog-add.component';
import { BlogEditComponent } from './blog-edit/blog-edit.component';
import { BlogGetComponent } from './blog-get/blog-get.component';
import { BlogGetoneComponent } from './blog-getone/blog-getone.component';
import { BlogSearchComponent } from './blog-search/blog-search.component'

const routes: Routes = [
  {
    path: 'create',
    component: BlogAddComponent
  },
  {
    path: 'edit/:id',
    component: BlogEditComponent
  },
  {
    path: 'post/:id',
    component: BlogGetoneComponent
  },
  {
    path: 'post',
    component: BlogGetComponent
  },
  {
    path: 'search',
    component: BlogSearchComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
