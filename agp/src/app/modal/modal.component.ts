import { Component, OnInit, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA} from '@angular/material';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
// import { PushNotificationsService} from 'ng-push';




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



  title = new FormControl('', [Validators.required, Validators.minLength(15)]);
  content = new FormControl('', [Validators.required, Validators.minLength(5)]);

  onNoClick(): void {
    this.dialogRef.close();
  }

  ngOnInit() {

  }

  getErrorMessage() {
    return this.title.hasError('required') ? 'You must enter a value' : '';
        // this.title.hasError('email') ? 'Not a valid email' : '';
  }

  // notify(){ //our function to be called on click
  //   let options = { //set options
  //     body: "The truth is, I'am Iron Man!"
  //   }
  //    this._pushNotifications.create('Iron Man', options).subscribe( //creates a notification
  //       res => console.log(res),
  //       err => console.log(err)
  //   );
  // }



}

