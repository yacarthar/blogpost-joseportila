import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-list-person',
  templateUrl: './list-person.component.html',
  styleUrls: ['./list-person.component.css']
})
export class ListPersonComponent implements OnInit {
  arrPeople = [
    {name: 'Ti', age: 10},
    {name: 'Tom', age: 30},
    {name: 'Taz', age: 20}
  ];
  constructor() { }
  removePerson(name: String) {
    const index = this.arrPeople.findIndex(x => x.name=== name);
    this.arrPeople.splice(index, 1);
  }
  ngOnInit() {
  }

}
