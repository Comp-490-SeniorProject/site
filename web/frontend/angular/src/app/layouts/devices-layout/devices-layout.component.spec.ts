import {ComponentFixture, TestBed} from "@angular/core/testing"

import {DevicesLayoutComponent} from "./devices-layout.component"

describe("DevicesLayoutComponent", () => {
    let component: DevicesLayoutComponent
    let fixture: ComponentFixture<DevicesLayoutComponent>

    beforeEach(async () => {
        await TestBed.configureTestingModule({
            declarations: [DevicesLayoutComponent],
        }).compileComponents()
    })

    beforeEach(() => {
        fixture = TestBed.createComponent(DevicesLayoutComponent)
        component = fixture.componentInstance
        fixture.detectChanges()
    })

    it("should create", () => {
        expect(component).toBeTruthy()
    })
})
