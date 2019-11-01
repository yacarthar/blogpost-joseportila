import { Component, OnInit, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA} from '@angular/material';


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

  onNoClick(): void {
    this.dialogRef.close();
  }

  ngOnInit() {
  }

}
