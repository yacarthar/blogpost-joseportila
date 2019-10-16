import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-form1',
  templateUrl: './form1.component.html',
  styleUrls: ['./form1.component.css']
})
export class Form1Component implements OnInit {
  name = '';
  constructor() { }
  evenStyle = {color: 'red', fontSize: '30px'};
  oddStyle = {color: 'black', fontSize: '20px'};
  flag = true;
  currentClass = {cirle: this.flag , square: !this.flag};
  ngOnInit() {
  }

}
