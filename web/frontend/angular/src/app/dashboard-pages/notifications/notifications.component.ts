import {Component, OnInit} from "@angular/core"
import {ApisService} from "src/app/apis/apis.service"
import * as $ from "jquery"

@Component({
    selector: "app-notifications",
    templateUrl: "./notifications.component.html",
    styleUrls: ["./notifications.component.scss"],
})
export class NotificationsComponent implements OnInit {
    constructor(private apiservice: ApisService) {}

    ngOnInit(): void {
        this.fetchTest()
    }

    addNotification(data: any) {
        this.apiservice.createNotification(data).subscribe(
            (res: any) => {
                console.log(res)
                if (res.status == 200) {
                    $("#notification").removeClass("d-none")
                    setTimeout(() => {
                        $("#notification").addClass("d-none")
                    }, 2000)
                    $("form").trigger("reset")
                } else {
                    $("input,select").addClass("error")
                    setTimeout(() => {
                        $("input,select").removeClass("error")
                    }, 2000)
                    $("form").trigger("reset")
                }
            },
            (error) => {
                console.log(error)
                $("input,select").addClass("error")
                setTimeout(() => {
                    $("input,select").removeClass("error")
                }, 2000)
                $("form").trigger("reset")
            }
        )
    }

    tests = []
    fetchTest() {
        this.apiservice.allTests().subscribe(
            (res: any) => {
                this.tests = res
                console.log(this.tests)
            },
            (error) => {
                console.log(error)
            }
        )
    }
}
