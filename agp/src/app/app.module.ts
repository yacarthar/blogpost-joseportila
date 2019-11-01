import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { HttpClientModule } from "@angular/common/http";
import { FormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {
  MatDialogModule,
  MatFormFieldModule,
  MatButtonModule,
  MatInputModule } from '@angular/material';

import { AppComponent } from './app.component';
import { ModalComponent } from './modal/modal.component';
import { BlogDetailComponent } from './blog-detail/blog-detail.component';
import { BlogListComponent } from './blog-list/blog-list.component';
import { ModalEditComponent } from './modal-edit/modal-edit.component';
import { ModalDeleteComponent } from './modal-delete/modal-delete.component';


@NgModule({
  declarations: [
    AppComponent,
    BlogDetailComponent,
    ModalComponent,
    BlogListComponent,
    ModalEditComponent,
    ModalDeleteComponent
  ],
  imports: [
    BrowserModule,
    // MaterialModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    FormsModule,
    MatDialogModule,
    MatFormFieldModule,
    MatButtonModule,
    MatInputModule
    // NgbModule
  ],

  bootstrap: [AppComponent],
  entryComponents: [ModalComponent, ModalEditComponent, ModalDeleteComponent]
})
export class AppModule { }
