import { Component, OnInit } from '@angular/core';
import { FormControl } from "@angular/forms";
import { Itunes2Service, SearchItem } from './itunes2.service';
import {
  debounceTime,
  distinctUntilChanged,
  switchMap,
  tap
} from "rxjs/operators";
import {Observable} from "rxjs";


@Component({
  selector: 'app-itunes2',
  templateUrl: './itunes2.component.html',
  styleUrls: ['./itunes2.component.css'],
  providers: [Itunes2Service]
})
export class Itunes2Component implements OnInit{
  private loading: boolean = false;
  private results: Observable<SearchItem[]>;
  private searchField: FormControl;

  constructor(private itunes: Itunes2Service) {}

  ngOnInit() {
    this.searchField = new FormControl();
    this.results = this.searchField.valueChanges.pipe(
      debounceTime(400),
      distinctUntilChanged(),
      tap(_ => (this.loading = true)),
      switchMap(term => this.itunes.search(term)),
      tap(_ => (this.loading = false))
    );
  }

  doSearch(term: string) {
    this.itunes.search(term);
  }
}
