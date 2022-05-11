import {Component, OnInit} from "@angular/core"
import {HttpClient} from "@angular/common/http"
import {FormBuilder} from "@angular/forms"

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
    deviceEndpoint = "api/devices/"

    devices: Devices[] | undefined

    addDeviceForm = this.formBuilder.group({
        name: "",
        description: "",
    })

    constructor(private http: HttpClient, private formBuilder: FormBuilder) {
        http.get<any[]>(`${this.deviceEndpoint}`, {
            headers: {},
        }).subscribe(
            (result) => {
                this.devices = result
            },
            (error) => console.error(error)
        )
    }

    ngOnInit(): void {}

    onSubmit() {
        const headers = {
            "Content-Type": "application/json",
        }

        const deviceInfo = JSON.stringify(this.addDeviceForm.value)

        this.http
            .post<any[]>(`${this.deviceEndpoint}`, deviceInfo, {headers})
            .subscribe()
        this.addDeviceForm.reset()
        this.http
            .get<any[]>(`${this.deviceEndpoint}`, {
                headers: {},
            })
            .subscribe(
                (result) => {
                    this.devices = result
                },
                (error) => console.error(error)
            )
    }
}
