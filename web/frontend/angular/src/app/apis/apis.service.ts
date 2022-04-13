import {Injectable} from "@angular/core"
import {HttpClient} from "@angular/common/http"
import {environment} from "src/environments/environment"

@Injectable({
    providedIn: "root",
})
export class ApisService {
    constructor(private http: HttpClient) {}

    alldevices() {
        return this.http.get(environment.baseUrl + "api/devices/")
    }

    allTests() {
        return this.http.get(environment.baseUrl + "api/tests/")
    }

    createNotification(data: any) {
        data.destination = [data.destination]
        console.log(data.destination)
        return this.http.post(
            environment.baseUrl + "api/notification_settings/",
            data
        )
    }
}
