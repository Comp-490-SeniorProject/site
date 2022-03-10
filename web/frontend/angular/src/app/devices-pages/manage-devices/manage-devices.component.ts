import {Component, OnInit} from "@angular/core"
import {HttpClient} from "@angular/common/http"

export class Devices {
    constructor(
        public id: number,
        public name: string,
        public description: string
    ) {}
}

@Component({
    selector: "app-manage-devices",
    templateUrl: "./manage-devices.component.html",
    styleUrls: ["./manage-devices.component.scss"],
})
export class ManageDevicesComponent implements OnInit {
    url = "http://127.0.0.1:8000/api/devices"

    devices: Devices[] | undefined

    constructor(http: HttpClient) {
        http.get<any[]>(`${this.url}`, {
            headers: {
                Accept: "application/json",
            },
        }).subscribe(
            (result) => {
                this.devices = result
            },
            (error) => console.error(error)
        )
    }

    ngOnInit(): void {}
}
