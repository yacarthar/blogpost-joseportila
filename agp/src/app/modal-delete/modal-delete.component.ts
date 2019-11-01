import { Component, OnInit, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA} from '@angular/material';

@Component({
  selector: 'app-modal-delete',
  templateUrl: './modal-delete.component.html',
  styleUrls: ['./modal-delete.component.css']
})
export class ModalDeleteComponent implements OnInit {

  constructor(
    public dialogRef: MatDialogRef<ModalDeleteComponent>)
    {}

  onNoClick(): void {
    this.dialogRef.close();
  }

  ngOnInit() {
  }
}
