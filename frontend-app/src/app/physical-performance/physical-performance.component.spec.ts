import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PhysicalPerformanceComponent } from './physical-performance.component';

describe('PhysicalPerformanceComponent', () => {
  let component: PhysicalPerformanceComponent;
  let fixture: ComponentFixture<PhysicalPerformanceComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PhysicalPerformanceComponent]
    });
    fixture = TestBed.createComponent(PhysicalPerformanceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
