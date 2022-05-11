import {Component, OnInit} from "@angular/core"
import {HttpClient} from "@angular/common/http"
import {FormBuilder} from "@angular/forms"

export interface Device {
    readonly id: number
    readonly name: string
    readonly description: string
}

interface NewDevice extends Device {
    aws: {
        readonly endpointAddress: string
        readonly certificateArn: string
        readonly certificateId: string
        readonly certificatePem: string
        readonly keyPair: {PublicKey: string; PrivateKey: string}
    }
}

@Component({
    selector: "app-manage-devices",
    templateUrl: "./manage-devices.component.html",
    styleUrls: ["./manage-devices.component.scss"],
})
export class ManageDevicesComponent implements OnInit {
    deviceEndpoint = "api/devices/"

    devices: Device[] = []

    addDeviceForm = this.formBuilder.group({
        name: "",
        description: "",
    })

    constructor(private http: HttpClient, private formBuilder: FormBuilder) {
        http.get<Device[]>(this.deviceEndpoint).subscribe(
            (devices: Device[]) => {
                this.devices = devices
            },
            (error) => console.error(error)
        )
    }

    ngOnInit(): void {}

    onSubmit() {
        this.http
            .post<NewDevice>(this.deviceEndpoint, this.addDeviceForm.value)
            .subscribe(
                (device: NewDevice) => {
                    this.devices.push(device)
                },
                (error) => console.error(error)
            )
        this.addDeviceForm.reset()
    }
}
