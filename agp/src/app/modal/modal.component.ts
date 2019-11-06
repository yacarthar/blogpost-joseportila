import { Component, OnInit, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA} from '@angular/material';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';

interface DialogData {
  title: string;
  content: string;
}

@Component({
  selector: 'app-modal',
  templateUrl: './modal.component.html',
  styleUrls: ['./modal.component.css']
})
export class ModalComponent implements OnInit {

  constructor(
    public dialogRef: MatDialogRef<ModalComponent>,
    @Inject(MAT_DIALOG_DATA) public data: DialogData) {}

  title = new FormControl('', [
    Validators.required,
    Validators.minLength(5),
    Validators.pattern("^[a-zA-Z0-9_-\\s]+$")
  ]);

  content = new FormControl('', [
    Validators.required,
    Validators.minLength(5),
    Validators.pattern("^[a-zA-Z0-9_-\\s\\(\\)\\.\\,]+$")
  ]);

  onNoClick(): void {
    console.log(this.data)
    this.dialogRef.close();
  }

  ngOnInit() {}



}

