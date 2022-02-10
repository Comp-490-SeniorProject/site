import {Component, OnInit} from "@angular/core"
import {Router} from "@angular/router"

@Component({
    selector: "app-devices-layout",
    templateUrl: "./devices-layout.component.html",
    styleUrls: ["./devices-layout.component.scss"],
})
export class DevicesLayoutComponent implements OnInit {
    title: string = ""
    checkURL: string = ""
    constructor(private route: Router) {}
    setHeader() {
        let path = this.route.url.split("/")[1]
        this.checkURL = decodeURIComponent(path)
        if (this.checkURL == "my-devices") {
            this.title = "Device Overview"
        } else if (this.checkURL == "manage-devices") {
            this.title = "Manage Devices"
        }
    }
    ngOnInit(): void {}
}
