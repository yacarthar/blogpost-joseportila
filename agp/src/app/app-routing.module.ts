import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { BlogAddComponent } from './blog-add/blog-add.component';
import { BlogEditComponent } from './blog-edit/blog-edit.component';
import { BlogGetComponent } from './blog-get/blog-get.component';
import { BlogGetoneComponent } from './blog-getone/blog-getone.component';

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
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
