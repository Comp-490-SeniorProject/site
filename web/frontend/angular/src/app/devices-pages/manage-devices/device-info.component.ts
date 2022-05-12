import {Component, Input} from "@angular/core"
import {NgbActiveModal} from "@ng-bootstrap/ng-bootstrap"
import {NewDevice} from "./models"

@Component({
    selector: "app-device-info",
    templateUrl: "./device-info.component.html",
})
export class DeviceInfoModalContent {
    @Input() newDevice: NewDevice | undefined

    constructor(public activeModal: NgbActiveModal) {}
}
