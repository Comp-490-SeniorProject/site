import {Injectable} from "@angular/core"
import {HttpClient} from "@angular/common/http"

@Injectable({
    providedIn: "root",
})
export class ApisService {
    constructor(private http: HttpClient) {}

    alldevices() {
        return this.http.get("http://0.0.0.0:8000/" + "api/devices/")
    }

    allTests() {
        return this.http.get("http://0.0.0.0:8000/" + "api/tests/")
    }

    createNotification(data: any) {
        data.destination = [data.destination]
        console.log(data.destination)
        return this.http.post(
            "http://0.0.0.0:8000/" + "api/notification_settings/",
            data
        )
    }
}
