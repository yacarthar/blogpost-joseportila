import { Component, OnInit } from '@angular/core';
import {IpService} from "./ip.service";


@Component({
    selector: 'app-ip',
    templateUrl: './ip.component.html',
    styleUrls: ['./ip.component.css'],
    providers: [IpService]
})
export class IpComponent implements OnInit {
    ip: String;
    constructor(private ipService: IpService) {}

    ngOnInit(): void {
     this.ipService.getIp()
         .then(ip => this.ip = ip)
    }

}
