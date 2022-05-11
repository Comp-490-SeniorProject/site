import {Component, OnInit} from "@angular/core"
import {HttpClient} from "@angular/common/http"
import {FormBuilder} from "@angular/forms"

export class Device {
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

    devices: Device[] | undefined

    addDeviceForm = this.formBuilder.group({
        name: "",
        description: "",
    })

    constructor(private http: HttpClient, private formBuilder: FormBuilder) {
        http.get<Device[]>(this.deviceEndpoint).subscribe(
            (result: Device[]) => {
                this.devices = result
            },
            (error) => console.error(error)
        )
    }

    ngOnInit(): void {}

    onSubmit() {
        this.http
            .post<Device>(this.deviceEndpoint, this.addDeviceForm.value)
            .subscribe()
        this.addDeviceForm.reset()
        this.http.get<Device[]>(this.deviceEndpoint).subscribe(
            (result: Device[]) => {
                this.devices = result
            },
            (error) => console.error(error)
        )
    }
}
