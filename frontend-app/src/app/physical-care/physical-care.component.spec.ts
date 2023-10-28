import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PhysicalCareComponent } from './physical-care.component';

describe('PhysicalCareComponent', () => {
  let component: PhysicalCareComponent;
  let fixture: ComponentFixture<PhysicalCareComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PhysicalCareComponent]
    });
    fixture = TestBed.createComponent(PhysicalCareComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
