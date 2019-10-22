import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { WordComponent } from './word/word.component';
import { BookComponent } from './book/book.component';
import { Form1Component } from './form1/form1.component';
import { StructComponent } from './struct/struct.component';
import { PersonComponent } from './person/person.component';
import { ListPersonComponent } from './list-person/list-person.component';
import { CardComponent} from './card.component';
import { IpComponent } from './ip/ip.component';
import { ItunesComponent } from './itunes/itunes.component';
import { BlogComponent } from './blog/blog.component';
import { Itunes2Component } from './itunes2/itunes2.component';
import { HttpClientModule } from "@angular/common/http";
import { platformBrowserDynamic } from "@angular/platform-browser-dynamic";
import { ReactiveFormsModule } from "@angular/forms";

@NgModule({
  declarations: [
    AppComponent,
    WordComponent,
    BookComponent,
    Form1Component,
    StructComponent,
    PersonComponent,
    ListPersonComponent,
    CardComponent,
    IpComponent,
    ItunesComponent,
    BlogComponent,
    Itunes2Component,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}
platformBrowserDynamic().bootstrapModule(AppModule)
