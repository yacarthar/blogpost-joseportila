import { Http} from '@angular/http'
import { Injectable }  from "@angular/core";

@Injectable()

export class IpService{
    constructor(private http: Http) {}
    getIp() {
        return this.http.get('http://127.0.0.1:5000/post')
        .toPromise()
        .then(res => res.json())
        .then(resJson => resJson.pagination.first_page);
    }

}