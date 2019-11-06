import { Component, OnInit, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA} from '@angular/material';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';

interface DialogData {
  title: string;
  content: string;
}

@Component({
  selector: 'app-modal-edit',
  templateUrl: './modal-edit.component.html',
  styleUrls: ['./modal-edit.component.css']
})
export class ModalEditComponent implements OnInit {

  constructor(
    public dialogRef: MatDialogRef<ModalEditComponent>,
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
    this.dialogRef.close();
  }

  ngOnInit() {}

}
