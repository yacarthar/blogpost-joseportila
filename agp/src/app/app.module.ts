import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { WordComponent } from './word/word.component';
import { BookComponent } from './book/book.component';
import { Form1Component } from './form1/form1.component';
import { StructComponent } from './struct/struct.component';
import { PersonComponent } from './person/person.component';
import { ListPersonComponent } from './list-person/list-person.component';
import { ParentComponent} from './parent.component';
import { ChildComponent} from './child.component';
import { CardComponent} from './card.component';
import { LearnPipeComponent } from './learn-pipe/learn-pipe.component';

@NgModule({
  declarations: [
    AppComponent,
    WordComponent,
    BookComponent,
    Form1Component,
    StructComponent,
    PersonComponent,
    ListPersonComponent,
    ParentComponent,
    ChildComponent,
    CardComponent,
    LearnPipeComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
