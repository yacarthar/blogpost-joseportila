import { Component, OnInit } from '@angular/core';
import { CchttpService } from './cchttp.service'

@Component({
  selector: 'app-cchttp',
  templateUrl: './cchttp.component.html',
  styleUrls: ['./cchttp.component.css'],
  providers: [CchttpService]
})
export class CchttpComponent implements OnInit {

  constructor(private cchttp: CchttpService) { }

  ngOnInit() {
  }

  doSearch(term:string) {
    this.cchttp.search(term)
  }
}
