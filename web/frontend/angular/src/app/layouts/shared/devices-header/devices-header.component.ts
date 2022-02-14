import {Component, OnInit} from "@angular/core"
import {Input} from "@angular/core"

@Component({
    selector: "app-devices-header",
    templateUrl: "./devices-header.component.html",
    styleUrls: ["./devices-header.component.scss"],
})
export class DevicesHeaderComponent implements OnInit {
    constructor() {}
    @Input() title: string = ""
    ngOnInit(): void {}
}
