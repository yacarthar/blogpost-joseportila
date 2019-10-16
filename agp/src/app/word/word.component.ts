import {Component} from '@angular/core';

@Component({
    templateUrl: './word.component.html',
    selector: 'app-word',
    styleUrls: ['./word.component.css']
})
export class WordComponent {
    en: string  = 'hello' ;
    vn: string = 'Xin chao';
    name = ''
    urls = 'https://image.shutterstock.com/image-photo/beautiful-water-drop-on-dandelion-600w-789676552.jpg'
    forgot = false;
    toggleForgot() {
        this.forgot = !this.forgot
    };
    showEvent(event) {
        console.log(event.target.value);
        this.name = event.target.value
    }

}
