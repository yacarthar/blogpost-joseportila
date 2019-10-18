import {Component, Output, EventEmitter} from '@angular/core';
// import { EventEmitter } from 'events';

@Component(
    {
        selector: 'app-child',
        template: `<h3><button (click)="addForParent()">Add</button> </h3>
        <h3><button (click)="subForParent()">Sub</button> </h3>`
    }
)

export class ChildComponent {
    @Output() myClick = new EventEmitter<boolean>();
    addForParent() {
        this.myClick.emit(true);
    }
    subForParent() {
        this.myClick.emit(false);
    }
}
