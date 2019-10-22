import { Component, OnInit } from '@angular/core';
import { SearchService } from './itunes.service'

@Component({
  selector: 'app-itunes',
  templateUrl: './itunes.component.html',
  styleUrls: ['./itunes.component.css'],
  providers: [SearchService]
})


export class ItunesComponent implements OnInit {
  private loading: boolean = false;

  constructor(private itunes:SearchService) { }

  doSearch(term:string) {
    this.loading = true;
    this.itunes.search(term).then( () => this.loading = false)
  }
  ngOnInit() {
  }

}
