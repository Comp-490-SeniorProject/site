import {Component, OnInit} from "@angular/core"
import {HttpClient} from "@angular/common/http"
import {FormBuilder} from "@angular/forms"
import {NgbModal} from "@ng-bootstrap/ng-bootstrap"
import {Device, NewDevice} from "./models"
import {DeviceInfoModalContent} from "./device-info.component"

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

    constructor(
        private http: HttpClient,
        private formBuilder: FormBuilder,
        private modalService: NgbModal
    ) {
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

                    const modal = this.modalService.open(
                        DeviceInfoModalContent,
                        {size: "lg"}
                    )
                    modal.componentInstance.newDevice = device
                },
                (error) => console.error(error)
            )
        this.addDeviceForm.reset()
    }
}
