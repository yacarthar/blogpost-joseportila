import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-struct',
  templateUrl: './struct.component.html',
  styleUrls: ['./struct.component.css']
})
export class StructComponent implements OnInit {

  constructor() { }
  filterStatus = 'all';
  isShow = true;
  newWord = '';
  definition = '';
  arrWords = [
    { id: 1, en: 'action', vn: 'hành động', memorized: true },
    { id: 2, en: 'actor', vn: 'diễn viên', memorized: false },
    { id: 3, en: 'activity', vn: 'hoạt động', memorized: true },
    { id: 4, en: 'active', vn: 'chủ động', memorized: true },
    { id: 5, en: 'bath', vn: 'tắm', memorized: false },
    { id: 6, en: 'bedroom', vn: 'phòng ngủ', memorized: true }
  ];
  addWord() {
    this.arrWords.unshift({
      id: this.arrWords.length + 1,
      en: this.newWord,
      vn: this.definition,
      memorized: false
    });
    this.newWord = '';
    this.definition = '';
  }
  deleteWord(id) {
    this.arrWords.splice(id - 1, 1);
  }
  getShowStatus(memorized: boolean) {
    const cond1 = this.filterStatus === 'all';
    const cond2 = this.filterStatus === 'memorized' && memorized;
    const cond3 = this.filterStatus === 'not memorized' && !memorized;
    return cond1 || cond2 || cond3;
  }
  ngOnInit() {
  }

}
