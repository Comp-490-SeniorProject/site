import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DevicesSidebarComponent } from './devices-sidebar.component';

describe('DevicesSidebarComponent', () => {
  let component: DevicesSidebarComponent;
  let fixture: ComponentFixture<DevicesSidebarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DevicesSidebarComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DevicesSidebarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
