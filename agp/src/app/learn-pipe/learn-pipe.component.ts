import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-learn-pipe',
  templateUrl: './learn-pipe.component.html',
  styleUrls: ['./learn-pipe.component.css']
})
export class LearnPipeComponent implements OnInit {

  constructor() { }
  birthday = new Date(2019, 10, 10);
  person = {name: 'tom', age: 20};
  address = Promise.raceesolve('92 street');


  ngOnInit() {
  }

}
