import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';

import { BlogService } from './blog.service';
import { BlogGetComponent } from './blog-get/blog-get.component';
import { BlogAddComponent } from './blog-add/blog-add.component';
import { BlogEditComponent } from './blog-edit/blog-edit.component';

import { HttpClientModule } from "@angular/common/http";
import { ReactiveFormsModule } from "@angular/forms";
import { SlimLoadingBarModule } from 'ng2-slim-loading-bar';
import { BlogGetoneComponent } from './blog-getone/blog-getone.component';

@NgModule({
  declarations: [
    AppComponent,
    BlogGetComponent,
    BlogAddComponent,
    BlogEditComponent,
    BlogGetoneComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    SlimLoadingBarModule,
    ReactiveFormsModule,
    HttpClientModule
  ],
  providers: [BlogService],
  bootstrap: [AppComponent]
})
export class AppModule {}
