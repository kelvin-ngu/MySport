import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MycommunityComponent } from './mycommunity.component';

describe('MycommunityComponent', () => {
  let component: MycommunityComponent;
  let fixture: ComponentFixture<MycommunityComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [MycommunityComponent]
    });
    fixture = TestBed.createComponent(MycommunityComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
