import { Component, OnInit, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA} from '@angular/material';

// interface DialogData {
//   del: boolean;
// }

@Component({
  selector: 'app-modal-delete',
  templateUrl: './modal-delete.component.html',
  styleUrls: ['./modal-delete.component.css']
})
export class ModalDeleteComponent implements OnInit {

  constructor(
    public dialogRef: MatDialogRef<ModalDeleteComponent>,
    @Inject(MAT_DIALOG_DATA) public data: boolean
  ) {}

  onNoClick(): void {
    this.data = false;
    // console.log(this.data)
    this.dialogRef.close();
  }

  ngOnInit() {
  }
}
