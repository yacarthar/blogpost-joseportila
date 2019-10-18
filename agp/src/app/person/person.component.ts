import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-person',
  templateUrl: './person.component.html',
  styleUrls: ['./person.component.css']
})
export class PersonComponent implements OnInit {

  constructor() { }
  @Input() name: string;
  @Input() age: number;
  @Output() removePerson = new EventEmitter<string>();
  ngOnInit() {
  }
  removeByClick() {
    this.removePerson.emit(this.name)
  }
}
